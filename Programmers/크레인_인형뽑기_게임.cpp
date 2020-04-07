#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
	int answer = 0;
	vector<int> v;
	for (int i = 0; i<moves.size(); i++) {
		for (int j = 0; j<board.size(); j++) {
			if (board[j][moves[i] - 1] != 0) {
				if (!v.empty() && board[j][moves[i] - 1] == v.back()) {
					answer += 2;
					v.pop_back();
				}
				else v.push_back(board[j][moves[i] - 1]);
				board[j][moves[i] - 1] = 0;
				break;
			}
		}
	}

	return answer;
}