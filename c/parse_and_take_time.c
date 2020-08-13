// um programa curto escrito como parte de algum outro projeto:
// - possivelmente acadêmico, relacionado a estruturas dados;
// - faz a leitura de um csv em C e toma o tempo de execução;
// - contém uma ou outra informação interessante quanto a leitura de arquivos em C e a time.h;


#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>


FILE *fp; // Ponteiro para abertura de arquivos.

char nome[100];
char dataPubAto[11];
char municipio[100];
char uf[3];
int counter = 0;

int main()
{

	setlocale(LC_ALL,NULL);

      // Cria uma variável do tipo fundamental clock_t:
      clock_t t;
      // Seta a variável t com o horário atual marcado em clock ticks (início da execução):
      t = clock();

      // Abre o arquivo para leitura:

      fp = fopen("Exemplo.csv", "r");

      // Seta o ponteiro do arquivo para a segunda linha, descartando a primeira:

      char descarte[200];
      fgets(descarte, sizeof(descarte), fp);

      // Faz a leitura do arquivo invocando a função de Inserção e passando os parâmetros:

      while(fscanf(fp, "%[^;];%[^;];%[^;];%s\n", nome, dataPubAto, municipio, uf) != EOF)
      {
            printf("%s\n", nome);
            printf("%s\n", dataPubAto);
            printf("%s\n", municipio);
            printf("%s\n\n", uf);
            counter++;

// Estas linhas são necessárias no programa final (removi o strupr():
//
//		no = criaNovoNo(nome, dataPubAto, municipio, uf);
//				r = adiciona(r,no);


      }

			// Fecha o arquivo aberto para leitura:
			fclose(fp);

			// Imprime a quantidade de entradas lidas:
      printf("-------------------------------------\nTotal de entradas lidas: %d\n",counter);

      // Seta a variável t com o horário atual (fim da execução) marcado em clock ticks e subtrai o horário do início de execução:
      t = clock() - t;

      // Imprime t dividido pela constante de sistema CLOCKS_PER_SEC para conseguir o tempo em segundos:
      printf ("Tempo de execução: %f segundos.\n",((float)t)/CLOCKS_PER_SEC);

}

