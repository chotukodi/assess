#include <iostream>
#include <fstream>
#include <string>
#include <vector>

class Question {
public:
    Question(const std::string& question, const std::vector<std::string>& choices, char correctAnswer)
        : question(question), choices(choices), correctAnswer(correctAnswer) {}

    void display() const {
        std::cout << question << std::endl;
        for (size_t i = 0; i < choices.size(); i++) {
            std::cout << static_cast<char>('A' + i) << ". " << choices[i] << std::endl;
        }
    }

    bool checkAnswer(char userChoice) const {
        return (toupper(userChoice) == correctAnswer);
    }

private:
    std::string question;
    std::vector<std::string> choices;
    char correctAnswer;
};

class Quiz {
public:
    void addQuestion(const Question& question) {
        questions.push_back(question);
    }

    void run() {
        int score = 0;
        for (const auto& question : questions) {
            question.display();

            char userChoice;
            std::cout << "Your answer: ";
            std::cin >> userChoice;

            if (question.checkAnswer(userChoice)) {
                score++;
            }

            std::cout << std::endl;
        }

        std::cout << "Quiz completed!" << std::endl;
        std::cout << "Your score: " << score << "/" << questions.size() << std::endl;
    }

private:
    std::vector<Question> questions;
};

int main() {
    Quiz quiz;

    std::ifstream file("quiz.txt");
    if (!file) {
        std::cerr << "Failed to open quiz file." << std::endl;
        return 1;
    }

    std::string line;
    std::vector<std::string> lines;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }
    file.close();

    for (size_t i = 0; i < lines.size(); i += 7) {
        std::string question = lines[i];
        std::vector<std::string> choices;
        for (size_t j = i + 1; j < i + 5; j++) {
            choices.push_back(lines[j].substr(3)); // Remove the choice prefix (e.g., "A. ")
        }
        char correctAnswer = lines[i + 5][0]; // Extract the first character of the answer line

        quiz.addQuestion(Question(question, choices, correctAnswer));
    }

    quiz.run();

    return 0;
}
