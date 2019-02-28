#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdio.h>

int Global;
int sleep_sec = 1;
pthread_mutex_t lock;

void *Thread1(void* x) {

	Global=1;
float sec=0.0;
 scanf("%f", &sec);
 if (sec >= 0 && sec <= 1) sleep(sec);
	pthread_mutex_lock(&lock);
	pthread_mutex_unlock(&lock);
  	return NULL;
}

void *Thread2(void* x) {
float sec=0.0;
 scanf("%f", &sec);
 if (sec >= 0 && sec <= 1) sleep(sec);
  pthread_mutex_lock(&lock);
  pthread_mutex_unlock(&lock);
  Global=2;
  return NULL;
}

int main(int argc, char *argv[])
{
	char input[100] = {0};
	char *out;

	// Slurp input
	if (read(STDIN_FILENO, input, 100) < 0) {
		fprintf(stderr, "Couldn't read stdin.\n");
	}
	if(input[0] == 'c') {
		// count characters
		out = malloc(sizeof(input) - 1 + 3); // enough space for 2 digits + a space + input-1 chars
		sprintf(out, "%lu ", strlen(input) - 1);
		strcat(out, input+1);
		printf("%s", out);
		free(out);
	} else if (strcmp(input, "\n") == 0) {
		  pthread_mutex_init(&lock, NULL);
		  pthread_t t[2];
		  pthread_create(&t[0], NULL, Thread1, NULL);
		  pthread_create(&t[1], NULL, Thread2, NULL);
		  pthread_join(t[0], NULL);
		  pthread_join(t[1], NULL);
		 pthread_mutex_destroy(&lock);
	} else {
		fprintf(stderr, "Usage: %s\nText utility - accepts commands on stdin and prints results to stdout:\n", argv[0]);
		fprintf(stderr, "\tInput           | Output\n");
		fprintf(stderr, "\t----------------+-----------------------\n");
		fprintf(stderr, "\tec<string>      | <string> (simple echo)\n");
		fprintf(stderr, "\thead<N><string> | The first <N> bytes of <string>\n");
		fprintf(stderr, "\tc<string>       | The length of <string>, followed by <string>\n");
		exit(1);
	}
}
