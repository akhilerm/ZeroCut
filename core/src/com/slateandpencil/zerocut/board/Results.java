package com.slateandpencil.zerocut.board;

import com.slateandpencil.zerocut.board.Cell.*;

/**
 * Created by Akhil on 06-11-2016.
 */

public class Results {
    public static final String TAG = Results.class.getName();

    Boolean hasWinner;
    CellValue winnerType;

    public Results() {
        this.hasWinner = Boolean.FALSE;
        this.winnerType = CellValue.EMPTY;
    }

    public CellValue getWinner() {
        return winnerType;
    }

    public Boolean hasWinner() {
        return hasWinner;
    }

    public void setWinner(CellValue winnerType) {
        this.winnerType = winnerType;
    }

    public void setHasWinner(Boolean hasWinner) {
        this.hasWinner = hasWinner;
    }
}
