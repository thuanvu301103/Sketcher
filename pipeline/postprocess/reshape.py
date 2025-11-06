import numpy as np

def reshape(contours):
    """
    Convert a list of 2D OpenCV contours into 3D vertex lists for Blender.

    Each contour (N,1,2) or (N,2) is converted to a list of [x, y, 0.0].
    """
    result = []
    for i, cnt in enumerate(contours):
        cnt2d = np.array(cnt, dtype=float)

        # Typical OpenCV contour shape is (N,1,2); squeeze safely
        if cnt2d.ndim == 3 and cnt2d.shape[1] == 1:
            cnt2d = cnt2d[:, 0, :]

        # If the contour collapses to a single point, reshape it
        if cnt2d.ndim == 1 and cnt2d.size == 2:
            cnt2d = cnt2d.reshape(1, 2)

        # Validate shape
        if cnt2d.ndim != 2 or cnt2d.shape[1] != 2:
            raise ValueError(f"Invalid contour shape {cnt2d.shape} at index {i}")

        # Convert to [x, y, 0.0]
        cnt3d = [[float(x), float(y), 0.0] for x, y in cnt2d]
        result.append(cnt3d)

    return result
