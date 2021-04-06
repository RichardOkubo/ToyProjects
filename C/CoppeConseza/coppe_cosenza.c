/** Modelo COPPE-COSENZA em C.
 *
 *  Utiliza uma única função: coppe_cosenza
 *
 *  Autor: Richard Okubo
 */

#include <stdio.h>

float coppe_cosenza(int i, int n, int *oferta, int *demanda);

int main(void)
{
    // EXEMPLO
    int oferta[]  = {1, 2, 1, 3, 3, 2, 2, 2, 1};
    int demanda[] = {2, 1, 1, 3, 2, 1, 1, 4, 3};

    // int n = sizeof(demanda) / sizeof(demanda[0]);
    int n = sizeof(oferta) / sizeof(oferta[0]);
    float resultado[n];

    for (int i = 0; i < n; i++)
        resultado[i] = coppe_cosenza(i, n, oferta, demanda);

    for (int j = 0; j < n; j++)
        printf("%f\n", resultado[j]);

    return 0;
}

/** Cruzamento entre oferta e demanda (com bonificação e penalização).
 *
 * LEGENDA:
 *     Avaliação dos fatores pela oferta:
 *         Excelente -> 1
 *         Bom -> 2
 *         Regular -> 3
 *         Insuficiente -> 4
 *
 *     Grau de satisfação dos fatores pela demanda:
 *         Crucial -> 1
 *         Condicionante -> 2
 *         Pouco condicionante -> 3
 *         Irrelevante -> 4
 */
float coppe_cosenza(int i, int n, int *oferta, int *demanda)
{
    float rank = 0.0;

    switch (demanda[i])
    {
        case 1:
            switch (oferta[i])
            {
                case 1:
                    rank = 1.0;
                    break;

                case 2:
                    rank = 1 - 1.0/n;
                    break;

                case 3:
                    rank = 1 - 2.0/n;
                    break;

                case 4:
                    rank = 1 - 3.0/n;
                    break;

                default:
                    break;
            }
            break;

        case 2:
            switch (oferta[i])
            {
                case 1:
                    rank = 1 + 1.0/n;
                    break;

                case 2:
                    rank = 1.0;
                    break;

                case 3:
                    rank = 1 - 1.0/n;
                    break;

                case 4:
                    rank = 1 - 2.0/n;
                    break;

                default:
                    break;
            }
            break;

        case 3:
            switch (oferta[i])
            {
                case 1:
                    rank = 1 + 2.0/n;
                    break;

                case 2:
                    rank = 1 + 1.0/n;
                    break;

                case 3:
                    rank = 1.0;
                    break;

                case 4:
                    rank = 1 - 1.0/n;
                    break;

                default:
                    break;
            }
            break;

        case 4:
            switch (oferta[i])
            {
                case 1:
                    rank = 1 + 3.0/n;
                    break;

                case 2:
                    rank = 1 + 2.0/n;
                    break;

                case 3:
                    rank = 1 + 1.0/n;
                    break;

                case 4:
                    rank = 1.0;
                    break;

                default:
                    break;
            }
            break;

        default:
            break;
    }

    return rank;
}
