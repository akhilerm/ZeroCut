package com.slateandpencil.zerocut.board;

/**
 * Created by Akhil on 06-11-2016.
 */

public class Results {
    public static final String TAG = Results.class.getName();

    Boolean hasWinner;
    Cell.CellValue winnerType;

    public Results() {
        this.hasWinner = Boolean.FALSE;
        this.winnerType = Cell.CellValue.EMPTY;
    }

    public Cell.CellValue getWinner() {
        return winnerType;
    }

    public Boolean hasWinner() {
        return hasWinner;
    }

    public void setWinner(Cell.CellValue winnerType) {
        this.winnerType = winnerType;
    }

    public void setHasWinner(Boolean hasWinner) {
        this.hasWinner = hasWinner;
    }
}
