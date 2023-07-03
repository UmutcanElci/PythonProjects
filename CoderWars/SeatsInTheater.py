def seats_in_theater(tot_cols, tot_rows, col, row):
    #your code here
    cols = tot_cols - (col-1)
    rows = tot_rows - row
    return cols * rows