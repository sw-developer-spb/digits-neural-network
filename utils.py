def convert_label_to_list(digit):
    label_list = [0] * 10
    label_list[digit] = 1
    return label_list


def convert_list_to_label(digit_list: list):
    for i in range(len(digit_list)):
        if digit_list[i] != 0:
            return i
    assert (True, "no 1 in digit_list")
    return 0


def make_flat_set(flat_im, flat_label):
    flat_set = list()
    for i in range(len(flat_im)):
        flat_set.append([flat_im[i], flat_label[i]])
    return flat_set


def convert_to_fraction(flat_im):
    res = list()
    koeff = 1 / 256
    for i in flat_im:
        res.append(flat_im[i] * koeff)
    return res


def convert_to_fraction2(np_array):
    koeff = 1 / 256
    for i in range(len(np_array)):
        np_array[i] = np_array[i] * koeff
