class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            img.reverse()
            for j in range(len(image[0])):
                if img[j] == 0:
                    img[j] = 1
                else:
                    img[j] = 0
        return image



        