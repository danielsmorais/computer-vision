#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

void swap(int*, int*);
void bubbleSort(int*, int);

    int main(int argc, char **argv)
{
    int ncoluna, nlinha;
    ncoluna = 1280;
    nlinha = 1057;
    Mat image, imedia(nlinha,ncoluna, CV_8UC1);

    String path;
    
    for (int k = 0; k < 9; k++)
    {
        path = "imagensComRuido_media/a" + to_string(k + 1) + ".jpg";

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

        path = "imagensSemRuido/a" + to_string(k + 1) + ".jpg";
        imwrite(path, imedia);
    }


    imshow("image", imedia);
    waitKey();
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

//RESPOSTA
// Como a imagem é composta por pixels de 8 bits, por ser tom de cinza a imagem poderá ter 256 diferentes tons. Retirando a cor de fundo (preta), temos 255 tons de cinza. Logo, se tivermos mais de 255 objetos não será possível rotulá-los na imagem. O interessante seria especificar um tom de cinza diferente de 0 e 255 e rotular todos os objetos. Com isso, não importa a quantidade de objetos.
