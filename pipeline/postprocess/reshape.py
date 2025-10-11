def reshape(contours):
    result = []
    for cnt in contours:
        cnt2d = cnt.squeeze()
        cnt3d = [[x, y, 0.0] for x, y in cnt2d]
        result.append(cnt3d)
    return result
