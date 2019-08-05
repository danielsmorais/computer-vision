#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main(int argc, char **argv)
{
    Mat image, mask;
    int width, height;
    int nobjects, noburacos;

    CvPoint p;
    image = imread("../imagens/bolhas.png", CV_LOAD_IMAGE_GRAYSCALE);

    if (!image.data) {
        cout << "Falha no carregamento." << endl;
        return (-1);
    }
    width = image.size().width; //colunas
    height = image.size().height;       //linhas

    p.x = 0;
    p.y = 0;
  
    imshow("image", image);
    imwrite("labeling.png", image);
    waitKey();
    return 0;
}




//RESPOSTA
// Como a imagem é composta por pixels de 8 bits, por ser tom de cinza a imagem poderá ter 256 diferentes tons. Retirando a cor de fundo (preta), temos 255 tons de cinza. Logo, se tivermos mais de 255 objetos não será possível rotulá-los na imagem. O interessante seria especificar um tom de cinza diferente de 0 e 255 e rotular todos os objetos. Com isso, não importa a quantidade de objetos.
