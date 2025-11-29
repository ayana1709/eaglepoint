// Step 3: Sleep helper function
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Step 3: Mock API function (unchanged)
async function mockFetch(url) {
  return new Promise((resolve, reject) => {
    const success = Math.random() > 0.3; // 70% success rate
    setTimeout(() => {
      if (success) resolve({ data: `Fetched data from ${url}` });
      else reject(new Error("Network error"));
    }, 300);
  });
}

// Step 3: Fetch with retry logic
async function fetchWithRetry(url, maxRetries = 3) {
  let attempt = 0;

  while (attempt < maxRetries) {
    try {
      console.log(`Attempt ${attempt + 1} to fetch ${url}`);
      const result = await mockFetch(url);
      return result; // Success
    } catch (error) {
      attempt++;
      console.warn(`Attempt ${attempt} failed: ${error.message}`);
      if (attempt === maxRetries) {
        throw new Error(
          `Failed to fetch data from ${url} after ${maxRetries} attempts`
        );
      }
      await sleep(1000); // Wait 1 second before retrying
    }
  }
}
