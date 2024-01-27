#this is a quiz game where user can give answer to a question.
#based on the answers will will get a score.


print("Welcome to my computer quiz game:")

game = input("Do you want to play the game(yes/no): ").lower()

answer_dict = {'What is the full form of ROM': 'read only memory',
               'What is the full form of RAM': 'random access memory'}

while game not in ('no'):

    if (game == 'yes'):
        print("Please answer the following questions:")

        score = 0
        #question 1
        answer = input("What is the full form of ROM: ").lower()

        if (answer == answer_dict['What is the full form of ROM']):
            score +=1

        #question 2
        answer = input("What is the full form of RAM: ").lower()

        if (answer == answer_dict['What is the full form of RAM']):
            score +=1
        

        #final result
        final_result = (100/2)*score
        print(f'you have got: {final_result}%')
        game = input("Do you want to play again(yes/no): ").lower()
    else:
        break
       
