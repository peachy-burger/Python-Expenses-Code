import java.util.Random;
import java.util.Scanner;

public class App {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		Random random = new Random();
		String[] choices = {"Rock", "Paper", "Scis"}; // Shortened "Scissors" to "Scis"
		System.out.println("\n Welcome to the game");
		while (true) {
			System.out.println("\n Choose Rock, Paper or Scissors (or type 'quit' to exit):");
			String playerInput = scanner.nextLine().trim();
			if (playerInput.equalsIgnoreCase("quit")) {
				System.out.println("\n You quit the game.");
				break;
			}
			int playerChoice = -1;
			for (int i = 0; i < choices.length; i++) {
				if (playerInput.equalsIgnoreCase(choices[i])) {
					playerChoice = i;
					break;
				}
			}
			if (playerChoice == -1) {
				System.out.println("Invalid choice or incorrect spelling. Please try again.");
				continue;
			}
			int computerChoice = random.nextInt(3);
			System.out.println("Computer threw: " + choices[computerChoice]);
			if (playerChoice == computerChoice) {
				System.out.println("Draw");
			} else if ((playerChoice == 0 && computerChoice == 2) ||
					   (playerChoice == 1 && computerChoice == 0) ||
					   (playerChoice == 2 && computerChoice == 1)) {
				System.out.println("You win!");
			} else {
				System.out.println("You lose!");
			}
		}
		scanner.close();
	}
}
