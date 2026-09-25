"""
Auto background removal utility using Pillow.
Uses flood-fill from corners to detect and remove background.
Works on white, grey, brown, dark — any solid/near-solid background.
Saves result as PNG with transparency.
"""
import io
import numpy as np
from PIL import Image


def remove_background(image_field, tolerance=40):
    """
    Remove background from a Django ImageField image.
    Returns a ContentFile with the processed PNG, or None on failure.
    """
    try:
        from django.core.files.base import ContentFile

        # Open image
        image_field.seek(0)
        img = Image.open(image_field).convert('RGBA')
        data = np.array(img, dtype=np.float32)

        h, w = data.shape[:2]
        r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

        # Sample background color from corners + edges
        sample_coords = [
            (0, 0), (0, w-1), (h-1, 0), (h-1, w-1),
            (0, w//2), (h//2, 0), (h-1, w//2), (h//2, w-1),
            (1, 1), (1, w-2), (h-2, 1), (h-2, w-2),
        ]
        bg_r = np.mean([data[y, x, 0] for y, x in sample_coords])
        bg_g = np.mean([data[y, x, 1] for y, x in sample_coords])
        bg_b = np.mean([data[y, x, 2] for y, x in sample_coords])

        # Color distance from background
        dist = np.sqrt(
            (r - bg_r) ** 2 +
            (g - bg_g) ** 2 +
            (b - bg_b) ** 2
        )

        # BFS flood fill from all 4 corners
        visited = np.zeros((h, w), dtype=bool)
        mask = np.zeros((h, w), dtype=bool)  # True = background

        from collections import deque
        queue = deque()

        for y, x in [(0,0), (0,w-1), (h-1,0), (h-1,w-1)]:
            if not visited[y, x]:
                visited[y, x] = True
                queue.append((y, x))

        while queue:
            y, x = queue.popleft()
            if dist[y, x] <= tolerance:
                mask[y, x] = True
                for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx]:
                        visited[ny, nx] = True
                        queue.append((ny, nx))

        # Apply transparency
        result = data.copy()
        # Fully transparent for background pixels
        result[mask, 3] = 0
        # Semi-transparent for near-background pixels (soft edges)
        near_bg = (~mask) & (dist < tolerance * 1.5)
        result[near_bg, 3] = (dist[near_bg] / (tolerance * 1.5) * 255).astype(np.float32)

        # Convert back to PIL and save as PNG
        out_img = Image.fromarray(result.astype(np.uint8), 'RGBA')

        # Resize to max 800px for performance
        max_size = 800
        if max(out_img.width, out_img.height) > max_size:
            ratio = max_size / max(out_img.width, out_img.height)
            new_size = (int(out_img.width * ratio), int(out_img.height * ratio))
            out_img = out_img.resize(new_size, Image.LANCZOS)

        buf = io.BytesIO()
        out_img.save(buf, format='PNG', optimize=True)
        buf.seek(0)
        return ContentFile(buf.read())

    except Exception as e:
        print(f'[BG Remover] Error: {e}')
        return None
