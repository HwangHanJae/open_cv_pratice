import cv2


def change_threshold_img(change_type, method, img_path):
    play_for_frame = 500
    #화면 위치 표시 좌표값
    x = 450
    y = 400
    #화면에 표시될 글씨 색
    black = (0, 0, 0)
    text_x = 150
    text_y = 40
    font = cv2.FONT_HERSHEY_SIMPLEX
    #원본 이미지
    image = cv2.imread(img_path)
    image_text = cv2.putText(image, "Original", (text_x, text_y),font , 1, black, 1, cv2.LINE_AA)
    cv2.imshow("image", image_text)
    cv2.moveWindow('image', x, y)
    #흑백 이미지
    image = cv2.imread(img_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray_text = cv2.putText(image_gray, "Gray", (text_x, text_y), font, 1, black, 1, cv2.LINE_AA)
    cv2.imshow("image_gray", image_gray_text)
    cv2.moveWindow('image_gray', x*2, y)
    #적응 임계점 처리방식
    if method == "m":
        method_c = cv2.ADAPTIVE_THRESH_MEAN_C
    elif method == "g":
        method_c = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    #blocksize = thresholding을 적용할 영역 사이즈
    if change_type == "size":
        start = 3
        end = 50
        fix_c = 3
        blk_sizes = []
        for i in range(start, end + 1):
            if i % 2 != 0:
                blk_sizes.append(i)
        n = len(blk_sizes)
        text_x -= 20
        for i in range(n):
            image = cv2.imread(img_path)
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            threshold = cv2.adaptiveThreshold(image_gray, 255, method_c, cv2.THRESH_BINARY, blk_sizes[i], fix_c)
            threshold_text = cv2.putText(threshold, "threshold {}".format(blk_sizes[i]), (text_x, text_y), font, 1, black, 1, cv2.LINE_AA)
            cv2.imshow('threshold', threshold_text)
            cv2.moveWindow('threshold', x*3, y)
            cv2.waitKey(play_for_frame)
    # blocksize = 평균이나 가중평균에서 차감할 값
    elif change_type == "c":
        start = 3
        end = 50
        cs = []
        fix_blk_size = 21
        for i in range(start, end + 1):
            if i % 2 != 0:
                cs.append(i)
        n = len(cs)
        text_x += 20
        for i in range(n):
            image = cv2.imread("test_image.webp")
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            threshold = cv2.adaptiveThreshold(image_gray, 255, method_c, cv2.THRESH_BINARY, fix_blk_size, cs[i])
            threshold_text = cv2.putText(threshold, "C {}".format(cs[i]), (text_x, text_y), font, 1, black, 1, cv2.LINE_AA)
            cv2.imshow('c', threshold_text)
            cv2.moveWindow('c', x*3, y)
            cv2.waitKey(play_for_frame)
    print("End")
    cv2.waitKey(0)
    return

type = "size"
method = "m"
#path = "hand_writing_image.jpg"
path = "images/test_image.webp"
change_threshold_img(change_type = type, method = method, img_path=path)

