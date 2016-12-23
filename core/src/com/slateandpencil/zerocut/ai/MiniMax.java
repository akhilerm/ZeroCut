package com.slateandpencil.zerocut.ai;

import com.slateandpencil.zerocut.board.Board;
import com.slateandpencil.zerocut.board.CellPosition;
import com.slateandpencil.zerocut.player.Player;

/**
 * Created by Akhil on 06-11-2016.
 */

public class MiniMax implements AI{
    public static final String TAG = MiniMax.class.getName();

    private class MinimaxResults {
        int bestScore;
        CellPosition bestposition;

        public MinimaxResults(MinimaxResults results) {
            this.bestScore = results.bestScore;
            this.bestposition = new CellPosition(results.bestposition);
        }

        public MinimaxResults(int bestScore, CellPosition bestposition) {
            this.bestScore = bestScore;
            this.bestposition = bestposition;
        }
    }

    public CellPosition determineBestPosition(Board board, Player forPlayer) {
        MinimaxResults results = miniMax(board, 2, Integer.MIN_VALUE, Integer.MAX_VALUE, forPlayer.getPlayerType());
        return results.bestposition;
    }

    private MinimaxResults miniMax(Board tempBoard, int depth, int alpha, int beta, Player.PlayerType playerType) {
        if (tempBoard.gameOver() || depth == 0) {
            return new MinimaxResults(tempBoard.getScore(), new CellPosition(-1, -1, -1, -1));
        }

        // playerX is trying to maximize, therefore we initialize to "-infinity" and begin looking for higher scores
        // playerO is trying to minimize, therefore we initialize to "+infinity" and begin looking for lower scores
        int bestScore = (playerType == Player.PlayerType.PLAYER_X) ? Integer.MIN_VALUE: Integer.MAX_VALUE;
        CellPosition bestPosition = new CellPosition(-1, -1, -1, -1);

        for(CellPosition position: tempBoard.emptyCellPositions()) {

            Board nextBoard = new Board(tempBoard.boardAfterMove(position, playerType.getCellValue()));

            if (playerType == Player.PlayerType.PLAYER_X) {
                MinimaxResults result = new MinimaxResults(miniMax(nextBoard, depth-1, alpha, beta, playerType.oppositePlayer()));
                if (result.bestScore > bestScore) {
                    bestScore = result.bestScore;
                    bestPosition = new CellPosition(position);
                }
                alpha = Math.max(alpha, result.bestScore);
                if (beta <= alpha) {
                    break;
                }
            } else {
                MinimaxResults result = new MinimaxResults(miniMax(nextBoard, depth-1, alpha, beta, playerType.oppositePlayer()));
                if (result.bestScore < bestScore) {
                    bestScore = result.bestScore;
                    bestPosition = new CellPosition(position);
                }
                beta = Math.min(beta, result.bestScore);
                if (beta <= alpha) {
                    break;
                }
            }
        }

        return new MinimaxResults(bestScore, bestPosition);
    }
}
