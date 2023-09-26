import gauss


def convolution(m, ker):
    """Операция свёртки numpy матриц"""

    return (m * ker).sum()


def normalize_matrix(m):
    matrix_sum = m.sum()

    def map_func(x):
        return x / matrix_sum

    return map_func(m)


def blur(image, d, sigm):
    x = image.shape[0]
    y = image.shape[1]

    result_image = image.copy()
    gaussian_kernel = normalize_matrix(gauss.create_gaussian_matrix(d, sigm))

    for i in range(x - d):
        for j in range(y - d):
            x_center = i + d // 2
            y_center = j + d // 2
            conv = convolution(image[i:i + d, j:j + d], gaussian_kernel)
            result_image[x_center, y_center] = conv

    return result_image
