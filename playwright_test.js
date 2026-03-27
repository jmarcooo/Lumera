const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    recordVideo: {
      dir: '/home/jules/verification/videos'
    }
  });
  const page = await context.newPage();

  // Test index.html
  await page.goto(`file://${path.resolve('index.html')}`);
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: '/home/jules/verification/screenshots/index.png', fullPage: true });

  // Test about.html
  await page.goto(`file://${path.resolve('about.html')}`);
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: '/home/jules/verification/screenshots/about.png', fullPage: true });

  // Test supplier-details.html
  await page.goto(`file://${path.resolve('supplier-details.html')}`);
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: '/home/jules/verification/screenshots/supplier-details.png', fullPage: true });

  await context.close();
  await browser.close();

  // Find video file
  const videoDir = '/home/jules/verification/videos';
  const files = fs.readdirSync(videoDir);
  const videoFile = files.find(f => f.endsWith('.webm'));

  console.log(JSON.stringify({
    indexScreenshot: '/home/jules/verification/screenshots/index.png',
    aboutScreenshot: '/home/jules/verification/screenshots/about.png',
    supplierScreenshot: '/home/jules/verification/screenshots/supplier-details.png',
    videoPath: videoFile ? path.join(videoDir, videoFile) : null
  }));
})();
