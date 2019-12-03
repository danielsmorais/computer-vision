#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

void swap(int *, int *);
void bubbleSort(int *, int);

int main(int argc, char **argv)
{
    int ncoluna, nlinha;
    ncoluna = 1280;
    nlinha = 1057;
    Mat image, imedia(nlinha,ncoluna, CV_8UC1);
    vector<Mat> all_images;
    int vv[9];

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

            for (size_t k = 0; k < 9; k++)
            {
                vv[k] = all_images[k].at<uchar>(i, j);
            }

            bubbleSort(vv, 9);

            imedia.at<uchar>(i, j) = vv[4]; // mediana
        }
    }

    path = "imagemSemRuido_mediana/a.jpg";
    imwrite(path, imedia);

    return 0;
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void bubbleSort(int *v, int n)
{
    if (n < 1)
        return;

    for (int i = 0; i < n; i++)
        if (v[i] > v[i + 1])
            swap(&v[i], &v[i + 1]);
    bubbleSort(v, n - 1);
}