function minimumRounds(tasks: number[]): number {

        const freq = new Map(
            tasks.map(x => [x, tasks.filter(y => y === x).length])
        );

        let result = 0;
        for (const count of freq.values()) {
            if (count === 1) {
                return -1;
            }
            result += Math.floor((count + 2) / 3);
        }

        return result;
    
}