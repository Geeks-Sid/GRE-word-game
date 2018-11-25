import string
from os.path import exists
import pandas as pd
from datetime import datetime
from random import shuffle
import numpy as np

if exists('D:\GRE\my word list\words.csv'):
    df = pd.read_csv('D:\GRE\my word list\words.csv')
    wordcount = df.shape[0]
else:
    df = pd.DataFrame(columns = ['word', 'meaning', 'date', 'times_correct', 'times_incorrect'])
    wordcount = 0


print("*****WELCOME*****")

def get_game():
    if exists('D:\GRE\my word list\high_score.csv'):
        high_df = pd.read_csv('D:\GRE\my word list\high_score.csv')
    else:
        high_df = pd.DataFrame(columns = ['score', 'date', 'time'])
        
    if exists('D:\GRE\my word list\words.csv'):
        df = pd.read_csv('D:\GRE\my word list\words.csv')
        wordcount = df.shape[0]
        if wordcount < 10:
            print('Sorry, the word list should atleast contain 10 words')
            return
    else:
        print('File doesnt exist!')
        return
    
    lives = 3
    score = 0
    datentime = datetime.now()
    new_date = datentime.strftime('%d-%m-%Y')
    new_time = datentime.strftime('%H-%M-%S')
    while(lives > 0):
        print('You have %d lives left!'%lives)
        word_index = np.random.randint(low = 0, high = wordcount)
        selected_word = df.iloc[word_index, 0]
        selected_word_meaning = df.iloc[word_index, 1]
        random_meanings = []
        random_meanings_index = np.random.randint(low = 0, high = wordcount, size = (4))
        for x in random_meanings_index:
            random_meanings.append(df.iloc[x, 1])
        random_meanings.append(selected_word_meaning)
        shuffle(random_meanings)
        print('\n', selected_word)
        for i in range(5):
            print('\n%d) %s'%(i, random_meanings[i]))
        while True:
            choice = int(input("\nEnter your choice!"))
            if choice in list(range(5)):
                break
            else:
                print('Wrong choice')
        if random_meanings[choice] == selected_word_meaning:
            score += 1
            print('Correct! Your score now is:', score)
            df.loc[word_index, 'times_correct'] += 1
        else:
            print('Sorry! Wrong answer')
            print('\n%s means %s'%(selected_word, selected_word_meaning))
            lives -= 1
            df.loc[word_index, 'times_incorrect'] += 1
    df.to_csv('D:\GRE\my word list\words.csv', index = False, columns = ['word', 'meaning', 'date', 'times_correct', 'times_incorrect'])
    print('Sorry, you just went out of lives, your highscore for %s at %s was %d'%(new_date, new_time, score))
    high_df.loc[high_df.shape[0]+1, :] = [score, new_date, new_time]
    high_df.sort_values(by = 'score', ascending = False)
    print(high_df)
    high_df.to_csv('D:\GRE\my word list\high_score.csv', index = False, columns = ['score', 'date', 'time'])
    return

def get_stats():
    print('Statistics')
    return

def get_meaning(get_word_meaning):
    if exists('D:\GRE\my word list\words.csv'):
        df = pd.read_csv('D:\GRE\my word list\words.csv')
        wordcount = df.shape[0]
    else:
        print('File doesnt exist!')
        return
    found = False
    for i in range(wordcount):
        if df.iloc[i, 0].lower == get_word_meaning.lower:
            print('\n%s means %s'%(get_word_meaning, df.iloc[i, 1]))
            found = True
            break
    if found == False:
        print('\nSorry, word was not found in your list')
    return

if __name__ == '__main__':
    
    choice = 1
    while(choice != '*'):
        print("1. Add new word\n2. Play word game\n3. Get word meaning\n4. Get Statistics\n*. TO EXIT!")
        print("\nEnter your choice!")
        choice = input()
        if choice == str(1):
            print("\nAdding new word!")
            new_word = input('\nPlease enter the word: ')
            word_meaning = input('\nPlease enter the meaning: ')
            date = datetime.now()
            date = date.strftime('%d-%m-%Y')
            corr = 0
            incorr = 0
            print('Number of words in list', wordcount+1)
            df.loc[wordcount, :] = [new_word, word_meaning, date, corr, incorr]
            wordcount += 1
            df.to_csv('D:\GRE\my word list\words.csv', index = False, columns = ['word', 'meaning', 'date', 'times_correct', 'times_incorrect'])
        elif choice == str(2):
            print("\nLets play word game!")
            get_game()
        elif choice == str(3):
            get_word_meaning = input('\nGetting word meaning, so please enter the word: ')
            get_meaning(get_word_meaning)
        elif choice == str(4):
            get_stats()
        elif choice == str('*'):
            df.to_csv('D:\GRE\my word list\words.csv', index = False, columns = ['word', 'meaning', 'date', 'times_correct', 'times_incorrect'])
            break
        else :
            print('\nWrong choice, Please try again')