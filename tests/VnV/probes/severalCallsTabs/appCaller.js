/**
 * Copyright 2017 Google Inc., PhantomJS Authors All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

'use strict';
const puppeteer = require('puppeteer');
const maxDuration = 90000;
(async() => {
  const browser = await puppeteer.launch({ headless:true,
                                            args: ['--use-fake-device-for-media-stream',
                                                   '--use-fake-ui-for-media-stream',
                                                   '--disable-notifications',
                                                   '--unsafely-allow-protected-media-identifier-for-domain',
                                                   '--no-sandbox']
                                          });
  //console.log("Inicio...");
  const page = await browser.newPage();
  await page.goto("https://comm-pilot.5gtango.eu/");
  await page.waitFor('input[name="username"]');
  await page.type('input[name="username"]', process.argv[2]);
  await page.waitFor('input[name="password"]');
  await page.type('input[name="password"]', process.argv[3]);
  await new Promise(done => setTimeout(done, 1000));
  await page.click('button[id="btn-login"]'); // With type

  //console.log("User logged...");
  await page.waitFor('input[class="search ng-pristine ng-untouched ng-valid ng-empty"]');
  await page.type('input[class="search ng-pristine ng-untouched ng-valid ng-empty"]',  process.argv[4]);
  await new Promise(done => setTimeout(done, 2000));
  if (await page.$('span[class="name"]', { timeout: 2000 }) == null){
    //console.log("No such user.");
    process.exit();
  }
  await page.waitFor('span[class="name"]');
  await page.click('span[class="name"]');

  await new Promise(done => setTimeout(done, 2000));
  await page.waitFor('button[class="btn btn-block btn-success"]');
  await page.click('button[class="btn btn-block btn-success"]');
  //console.log("Calling...");
  try {
    await new Promise(done => setTimeout(done, 20000));
    if (await page.$('button[class="hang-up"]') !== null){
      //console.log("On Call");
      await new Promise(done => setTimeout(done, process.argv[5]));
    }
    await page.waitFor('button[class="hang-up"]', { timeout: 5000 });
    await page.click('button[class="hang-up"]'); // With type
    //console.log("Call finished successfully");
    process.exit();

  }catch (e) {
    //console.log("The called user is not avaliable.");
    process.exit();
  }


})();
