function twoSum(nums: number[], target: number): number[] {
    let map = new Map()
    
    for (let i = 0; i < nums.length; i++) {
        let val = nums[i];
        let compliment = target - val;
        
        if (map.has(compliment)) {
                return [map.get(compliment), i]
        } else {
            map.set(val, i)
        }
    }
    return []
};