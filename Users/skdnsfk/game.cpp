#include <iostream>
#include <time.h>
#include <cstdlib>
using namespace std;

bool Compare ( char* answer, char* number , int input)
{
        bool return_value = true;
        for ( int i = 0 ; i < input * input - 1 ; i++)
                if ( answer[i+1] != number[i] ) return_value = false;
        return return_value;

}
void Swap ( char &a, char &b)
{
        char tmp;
        tmp = a;
        a = b;
        b = tmp;
}

void Print_Tile ( char* number, int input )
{
        int index = 0;
        for ( int i = 0 ; i < input; i++)
        cout << " ---";
        for ( int i = 0 ; i < input  ; i++)
        {
                cout << endl << "| ";
                for ( int j = 0 ; j < input ; j++)
                {
                        cout << number[index] << " | ";
                        index++;
                }
                cout << endl;
                for ( int j = 0 ; j < input ; j++)
                        cout << " ---";
        }
        cout << endl;
}
void Moving_Tile ( char* number, char* answer, int input)
{
        char direction;
        int current_position = 0;
        while ( 1 )
        {
                Print_Tile ( number, input );
                if ( Compare ( answer, number ,input ) )
                {
                        cout << "Complete! Exiting program." << endl;
                        break;
                }
                cout << "Slide the empty cell [u,d,l,r]:";
                cin >> direction;
                if ( direction == 'u' )
                {
                        if ( current_position < input )
                        {
                                cout << "Invalid direction." << endl;
                                continue;
                        }
                        Swap ( number[current_position], number[current_position-input] );
                        current_position -= input;
                }
                else if ( direction == 'd' )
                {
                        if ( current_position > input * input - input - 1 )
                        {
                                cout << "Invalid direction." << endl;
                                continue;
                        }
                        Swap ( number[current_position], number[current_position+input] );
                        current_position += input;
                }
                else if ( direction == 'l' )
                {
                        if ( current_position % input == 0 )
                        {
                                cout << "Invalid direction." << endl;
                                continue;
                        }
                        Swap ( number[current_position], number[current_position-1] );
                        current_position -= 1;
                }
                else if ( direction == 'r' )
                {
                        if ( current_position % input == input - 1 )
                        {
                                cout << "Invalid direction." << endl;
                                continue;
                        }
                        Swap ( number[current_position], number[current_position+1] );
                        current_position += 1;
                }
                else
                {
                        cout << "Invalid direction." << endl;
                        continue;
                }
        }
}
int main()
{
int seed_value = 0;
int input = 0;
        cout << "Welcome to Sliding Tiles!" << endl;
        while (1)
        {
                cout << "Choose a board size [3+]:";
                cin >> input;
                if ( input < 3 )
                {
                        cout << input << " is not a valid input." << endl;
                        continue;
                }
                else if ( input > 4 )
                {
                        cout << input << " is not supported." << endl;
                        continue;
                }
                cout << "Input a seed value:";
                cin >> seed_value;
                break;
        }
        srand ( seed_value );
char* number = new char [ input * input ];
char* answer = new char [ input * input ];
char tmp = '0';
        number[0] = ' ';
        for ( int i = 1; i < input * input ; i++)
                number[i] = ( ( rand() % 10 ) ) + '0';
        for ( int i = 0 ; i < input * input ; i++)
                answer[i] = number[i];
        for ( int i = 0 ; i < input * input - 1 ; i++)
        {
                for ( int j = 0 ; j < input*input - i - 1 ; j++)
                {
                        if ( answer[j] > answer[j+1] )
                        {
                                tmp = answer[j];
                                answer[j] = answer[j+1];
                                answer[j+1] = tmp;
                        }
                }
        }
        Moving_Tile ( number, answer, input);

        delete number;
        delete answer;
}