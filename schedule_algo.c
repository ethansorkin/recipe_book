/* Algorithm to organize a fantasy basketball schedule




*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <schedule_algo.h>

struct Game
{
    char *home;
    char *away;
    char *gametime;
};

struct Day
{
    Game *games;
};

struct Player
{
    char *team;

};


struct Team
{
    char *user;
    char *name;
    Day *days;
    Player *roster;
};

struct League
{
    Team *teams;
};

int main() 
{

}

int numCommonGames (Team team1, Team team2) {
    if (team)
}