typdef struct Mutex{
    int turn;
    int* waiting;
    int num_processes;
}Mutex;

