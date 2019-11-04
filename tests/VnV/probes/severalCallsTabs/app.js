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
var exec = require('child_process').exec, child;
const maxDuration = 90000;
(async() => {
  const browser = await puppeteer.launch({ headless:true,
                                            args: ['--use-fake-device-for-media-stream',
                                                   '--use-fake-ui-for-media-stream',
                                                   '--disable-notifications',
                                                   '--unsafely-allow-protected-media-identifier-for-domain',
						   '--disable-webrtc-encryption',
                                                   '--no-sandbox']
					    //slowMo:50
                                        });
var x;
var index;
var indexCallee;
var numTabs = process.argv[2]*2;
console.log("TABS")
console.log(numTabs);
for (x = 0; x < numTabs; x++) {
  this["page"+x] = await browser.newPage();
  await this["page"+x].goto("https://comm-pilot.5gtango.eu/");
}
index = process.argv[3]
for (x = 0; x < numTabs; x=x+2) {
  console.log("Entra");
  console.log(index);
  //CALLED

  await this["page"+x].bringToFront();
  await this["page"+x].waitFor('input[name="username"]');
  await this["page"+x].type('input[name="username"]',  "5gtango"+index);
  await this["page"+x].waitFor('input[name="password"]');
  await this["page"+x].type('input[name="password"]', "5gtango"+index);
  await new Promise(done => setTimeout(done, 1000));
  await this["page"+x].click('button[id="btn-login"]');
  indexCallee=index-1;
  //CALLEE
 
  await this["page"+(x+1)].bringToFront();
  await this["page"+(x+1)].waitFor('input[name="username"]');
  await this["page"+(x+1)].type('input[name="username"]', "5gtango"+indexCallee);
  await this["page"+(x+1)].waitFor('input[name="password"]');
  await this["page"+(x+1)].type('input[name="password"]', "5gtango"+indexCallee);
  await this["page"+(x+1)].click('button[id="btn-login"]');
  await this["page"+(x+1)].waitFor('input[class="search ng-pristine ng-untouched ng-valid ng-empty"]');
  await this["page"+(x+1)].type('input[class="search ng-pristine ng-untouched ng-valid ng-empty"]',  "5gtango"+(index));
  await new Promise(done => setTimeout(done, 1000));
  await this["page"+(x+1)].waitFor('span[class="name"]');
  await this["page"+(x+1)].click('span[class="name"]');
  await new Promise(done => setTimeout(done, 1000));
  await this["page"+(x+1)].waitFor('button[class="btn btn-block btn-success"]');
  await this["page"+(x+1)].click('button[class="btn btn-block btn-success"]');

  //CALLED
  await this["page"+x].bringToFront();
  await this["page"+x].waitFor('button[class="pick-up"]');
  await this["page"+x].click('button[class="pick-up"]');

  console.log("CALL ESTABLISHED")
  index = index - 2;
}

})();
