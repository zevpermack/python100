var isPalindrome = function(x) {
  console.log(typeof x)
  for (let i = 0; i < x.length; i++) {
    console.log('run')
      const beginningIndex = x[i];
      const endIndex = x[x.length -1 - i]
      if (beginningIndex !== endIndex) {
          return false
      }
  }
  console.log("run")
  return true;
};

console.log(isPalindrome("121"));