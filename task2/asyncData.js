// Helper function
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Mock API function to work with network request
async function mockFetch(url) {
  return new Promise((resolve, reject) => {
    const success = Math.random() > 0.3;
    setTimeout(() => {
      if (success) resolve({ data: `Fetched data from ${url}` });
      else reject(new Error("Network error"));
    }, 300);
  });
}

/**
 * Fetch data with retry logic
 * @param {string} url
 * @param {number} maxRetries
 * @returns {Promise<Object>}
 * @throws {Error}
 */
async function fetchWithRetry(url, maxRetries = 3) {
  let attempt = 0;

  while (attempt < maxRetries) {
    try {
      console.log(`Attempt ${attempt + 1} to fetch ${url}`);
      const result = await mockFetch(url);
      return result;
    } catch (error) {
      attempt++;
      console.warn(`Attempt ${attempt} failed: ${error.message}`);

      if (attempt === maxRetries) {
        // All retries exhausted, throw final error
        throw new Error(
          `Failed to fetch data from ${url} after ${maxRetries} attempts`
        );
      }

      await sleep(1000);
    }
  }
}
(async () => {
  const testUrl = "https://jsonplaceholder.typicode.com/todos";

  try {
    const data = await fetchWithRetry(testUrl, 5);
    console.log("Success:", data);
  } catch (error) {
    console.error("Final Error:", error.message);
  }
})();
