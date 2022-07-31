
Algorithm

- Reduce B to a single word bmax as described above, then compare the counts of letters between words a in A, and bmax.

For example, when checking whether "warrior" is a superset of words B = ["wrr", "wa", "or"], we can combine these words in B to form a "maximum" word "arrow", that has the maximum count of every letter in each word in B.