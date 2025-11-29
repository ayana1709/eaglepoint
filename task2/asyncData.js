async function mockFetch(url) {
  return new Promise((resolve, reject) => {
    const success = Math.random() > 0.3;
    setTimeout(() => {
      if (success) resolve({ data: `Fetched data from ${url}` });
      else reject(new Error("Network error"));
    }, 300);
  });
  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}
