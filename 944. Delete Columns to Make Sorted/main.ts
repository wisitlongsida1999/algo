class Solution {
  minDeletionSize(strs: string[]): number {
    let countCol = 0;
    for (let i = 0; i < strs[0].length; i++) {
      let prev = strs[0][i];
      let curr = "";
      for (let j = 1; j < strs.length; j++) {
        curr = strs[j][i];
        if (prev > curr) {
          countCol++;
          break;
        } else {
          prev = curr;
        }
      }
    }
    return countCol;
    }
}

