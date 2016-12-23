package com.slateandpencil.zerocut.player;

import com.slateandpencil.zerocut.board.Board;
import com.slateandpencil.zerocut.board.CellPosition;

/**
 * Created by Akhil on 06-11-2016.
 */

public class HumanPlayer extends Player {
    public static final String TAG = HumanPlayer.class.getName();

    public HumanPlayer(Board board, PlayerType type) {
        super(board, type);
    }

    public CellPosition setCellAtPosition(CellPosition position) {
        getBoard().setCell(position, this.getPlayerType().getCellValue());   /// Changes may be required here, setCell return boolean to check whether cell already taken.
        return position;
    }

}
