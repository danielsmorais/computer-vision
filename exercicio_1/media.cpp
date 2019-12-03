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

    vector<Mat> all_images;

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

        all_images.push_back(image);
    }

    for (int i = 0; i < nlinha; i++)
    {
        for (int j = 0; j < ncoluna; j++)
        {
            int aux=0;

            for (size_t k = 0; k < 9; k++)
            {
                aux = aux + all_images[k].at<uchar>(i, j);
            }            

            imedia.at<uchar>(i, j) = aux/9;
        }
    }

    path = "imagemSemRuido_media/a.jpg";
    imwrite(path, imedia);

    return 0;
}