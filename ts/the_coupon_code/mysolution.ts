export function checkCoupon(enteredCode: string, correctCode: string, currentDate: string, expirationDate: string): boolean {
  const isCodeValid = enteredCode === correctCode;
  const isNotExpired = new Date(currentDate).getTime() <= new Date(expirationDate).getTime();
  return isCodeValid && isNotExpired;
}

// original kata: https://www.codewars.com/kata/539de388a540db7fec000642
// my solution: https://www.codewars.com/kata/reviews/58058cc3eb22f7889f000015/groups/6a54998a948b691f8b82cedd
