# week06 -> test_scores.py

def main():
    print("Welcome to the Test Scores Program")

    total_score = 0
    num_scores = 0
    
    while True:
        score = input("Enter a test score (or 999 to finish): ")
        
        if not score.isdigit():
            print("Invalid entry. Please enter a valid test score between 0 and 100 or 999 to finish.")
            continue

        score = int(score)
        
        if score == 999:
            break
        
        if score < 0 or score > 100:
            print("Invalid entry. Please enter a valid test score between 0 and 100.")
        else:
            total_score += score
            num_scores += 1
    
    if num_scores > 0:
        average_score = total_score / num_scores
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score:.2f}")
    else:
        print("No valid test scores were entered.")

if __name__ == "__main__":
    main()
