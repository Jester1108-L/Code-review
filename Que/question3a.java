import java.util.Scanner;

class question3a{
	
	
	public static void main(String[] args){
		boolean again = true;
		while (again){
			playGame();	
			Scanner reader = new Scanner(System.in);
			System.out.print("Would you like to play again: (y/n)");
			String retry = reader.nextLine();
			while((!retry.equals("y")) && (!retry.equals("n"))){
				System.out.print("Would you like to play again: (y/n)");
				retry = reader.nextLine();
			}
			if(retry.equals("n")){
				again = false;
			}
		}
	}
	
	private static void display(String[][] board){
		System.out.println("-------");
		for(int i=0; i<3; i++){
			String temp = "";
			for(int j=0; j<3; j++){
				temp = temp + "|" + board[i][j];
			}
			temp = temp + "|";
			System.out.println(temp);
			System.out.println("-------");
		}
	}
	
	private static void playGame(){
		Scanner reader = new Scanner(System.in);
		String[][] board = new String[3][3];
		for(int i=0; i<3; i++){
			String temp = "|";
			for(int j=0; j<3; j++){
				board[i][j] = " ";
			}
		}
		boolean turn = true;
		int row = 0;
		int col = 0;
		String piece = "";
		boolean correctDigit = true;
		while (!checkWin(board, piece) && !notFull(board)){
			correctDigit = true;
			display(board);
			if (turn){
				piece = "x";
			}
			else{
				piece = "0";
			}
			System.out.print("Player " + piece + ", please enter a row (0, 1 or 2): ");
			row = Integer.parseInt(reader.nextLine());
			System.out.print("Player " + piece + ", please enter a column (0, 1 or 2): ");
			col = Integer.parseInt(reader.nextLine());
			if((row > 2) || (row < 0) || (col > 2) || (col < 0)){
				correctDigit = false;
			}
			while(!correctDigit){
				System.out.println("Wrong row/column has been given. Please try again");
				System.out.print("Player " + piece + ", please enter a row (0, 1 or 2): ");
				row = Integer.parseInt(reader.nextLine());
				System.out.print("Player " + piece + ", please enter a column (0, 1 or 2): ");
				col = Integer.parseInt(reader.nextLine());
				correctDigit = true;
				if((row > 2) || (row < 0) || (col > 2) || (col < 0)){
				correctDigit = false;
			}
			}
			while(!board[row][col].equals(" ")){
				System.out.println("Spot has been taken. Please try again");
				System.out.print("Player " + piece + ", please enter a row (0, 1 or 2): ");
				row = Integer.parseInt(reader.nextLine());
				System.out.print("Player " + piece + ", please enter a column (0, 1 or 2): ");
				col = Integer.parseInt(reader.nextLine());
			}
			board[row][col] = piece;
			turn = !turn;
		}
		display(board);
		if(notFull(board)){
			System.out.println("The game is a draw.");
		}
		else{
			System.out.println("Congratulations, player " + piece + " has won the game!");
		}
	}
	
	private static boolean notFull(String[][] board){
		for(int i=0; i<3; i++){
			for(int j=0; j<3; j++){
				if(board[i][j].equals(" ")){
					return false;
				}
			}
		}
		return true;
	}
	
	private static boolean checkWin(String[][] board, String piece){
		if((board[0][0].equals(piece)) & (board[0][1].equals(piece))  & (board[0][2].equals(piece))){
			return true;
		}
		if((board[1][0].equals(piece)) & (board[1][1].equals(piece))  & (board[1][2].equals(piece))){
			return true;
		}
		if((board[2][0].equals(piece)) & (board[2][1].equals(piece))  & (board[2][2].equals(piece))){
			return true;
		}
		if((board[0][0].equals(piece)) & (board[1][0].equals(piece))  & (board[2][0].equals(piece))){
			return true;
		}
		if((board[0][1].equals(piece)) & (board[1][1].equals(piece))  & (board[2][1].equals(piece))){
			return true;
		}
		if((board[0][2].equals(piece)) & (board[1][2].equals(piece))  & (board[2][2].equals(piece))){
			return true;
		}
		if((board[0][0].equals(piece)) & (board[1][1].equals(piece))  & (board[2][2].equals(piece))){
			return true;
		}
		if((board[0][2].equals(piece)) & (board[1][1].equals(piece))  & (board[2][0].equals(piece))){
			return true;
		}
		return false;
	}
}