#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main(int argc, char **argv)
{
    int ncoluna, nlinha;
    ncoluna = 1280;
    nlinha = 1057;
    Mat image, imedia(nlinha,ncoluna, CV_8UC1);

    String path;
    
    for (int k = 0; k < 9; k++)
    {
        path = "imagensComRuido/a" + to_string(k + 1) + ".jpg";

        image = imread(path, CV_LOAD_IMAGE_GRAYSCALE);
        if (!image.data)
        {
            cout << "Falha no carregamento." << endl;
            return (-1);
        }

        for (int i = 1; i < nlinha-1; i++)
        {
            for (int j = 1; j < ncoluna-1; j++)
            {
                imedia.at<uchar>(i, j) = image.at<uchar>(i - 1, j - 1) / 9 + image.at<uchar>(i - 1, j) / 9 + image.at<uchar>(i - 1, j + 1) / 9 +
                                         image.at<uchar>(i, j - 1) / 9 + image.at<uchar>(i, j) / 9 + image.at<uchar>(i, j + 1) / 9 +
                                         image.at<uchar>(i + 1, j - 1) / 9 + image.at<uchar>(i + 1, j) / 9 + image.at<uchar>(i + 1, j + 1) / 9;
            }            
        }

        path = "imagensSemRuido_media/a" + to_string(k + 1) + ".jpg";
        imwrite(path, imedia);
    }

    return 0;
}