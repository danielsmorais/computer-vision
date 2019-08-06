#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main(int argc, char **argv)
{
    int ncoluna, nlinha;
    Mat image;

    float lap[] = {0,  1,  0,
                 1,  -4,  1,
                 0,  1,  0};

    String path = "original.png";

    image = imread(path, CV_LOAD_IMAGE_GRAYSCALE);
    if (!image.data)
    {
        cout << "Falha no carregamento." << endl;
        return (-1);
    }

    ncoluna = image.size().width;
    nlinha = image.size().height;

    Mat ilaplace(nlinha, ncoluna, CV_8UC1);

    for (int i = 1; i < nlinha - 1; i++)
    {
        for (int j = 1; j < ncoluna - 1; j++)
        {
            ilaplace.at<uchar>(i, j) = image.at<uchar>(i - 1, j - 1) * lap[0] / 9 + image.at<uchar>(i - 1, j) * lap[1] / 9 + image.at<uchar>(i - 1, j + 1) * lap[2] / 9 +
                                       image.at<uchar>(i, j - 1) * lap[3] / 9 + image.at<uchar>(i, j) * lap[4] / 9 + image.at<uchar>(i, j + 1) * lap[5] / 9 +
                                       image.at<uchar>(i + 1, j - 1) * lap[6] / 9 + image.at<uchar>(i + 1, j) * lap[7] / 9 + image.at<uchar>(i + 1, j + 1) * lap[8] / 9;
        }
    }

    path = "imagensLaplaciano/laplace.jpg";
    imwrite(path, ilaplace);
    
    return 0;
}