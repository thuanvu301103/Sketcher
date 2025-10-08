def reshape(contours):
    result = []
    for cnt in contours:
        cnt2d = cnt.squeeze()
        result.append(cnt2d)
    return result