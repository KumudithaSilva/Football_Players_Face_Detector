
def classify_image(image_based64, file_path=None):
    pass

def get_b64_test_image():
    with open("b64.txt", 'r') as file:
        return file.read()

if __name__ == '__main__':
    print(classify_image(get_b64_test_image(), None))