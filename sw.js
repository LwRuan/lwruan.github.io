if(!self.define){let e,s={};const i=(i,r)=>(i=new URL(i+".js",r).href,s[i]||new Promise((s=>{if("document"in self){const e=document.createElement("script");e.src=i,e.onload=s,document.head.appendChild(e)}else e=i,importScripts(i),s()})).then((()=>{let e=s[i];if(!e)throw new Error(`Module ${i} didn’t register its module`);return e})));self.define=(r,l)=>{const n=e||("document"in self?document.currentScript.src:"")||location.href;if(s[n])return;let a={};const t=e=>i(e,n),u={module:{uri:n},exports:a,require:t};s[n]=Promise.all(r.map((e=>u[e]||t(e)))).then((e=>(l(...e),a)))}}define(["./workbox-f51ab5e4"],(function(e){"use strict";self.skipWaiting(),e.clientsClaim(),e.precacheAndRoute([{url:"assets/_...all_.b1501b98.js",revision:null},{url:"assets/_name_.59fe4a3f.js",revision:null},{url:"assets/2022-08-15-games.21350f4f.js",revision:null},{url:"assets/404.37573b32.js",revision:null},{url:"assets/app.4e85bc41.js",revision:null},{url:"assets/home.baebf0b6.js",revision:null},{url:"assets/index.4e932688.js",revision:null},{url:"assets/index.9f62de97.css",revision:null},{url:"assets/pbd-st.f2957fe4.js",revision:null},{url:"assets/README.01608abc.js",revision:null},{url:"assets/virtual_pwa-register.3ff79d29.js",revision:null},{url:"assets/waterstrider.8505a628.js",revision:null},{url:"blogs.html",revision:"72fd3a67266ff514089c6a13e4960d3d"},{url:"blogs/2022-08-15-games.html",revision:"5ab2d03f9978bc63051246a0a281cf5b"},{url:"index.html",revision:"a24ef6e130d800e602ef5b7e854fc4fa"},{url:"pubs/pbd-st.html",revision:"94cb6e6ce7a001a089112aba14db9163"},{url:"pubs/waterstrider.html",revision:"c01c341ee93239fa73205656a5da16d8"},{url:"readme.html",revision:"a1a93ade37770e2888c31bf1eb185d45"},{url:"favicon.svg",revision:"a795ab195c26601ea433babed25a7d0d"},{url:"safari-pinned-tab.svg",revision:"5eaf74d1c43d30e0af743b68a3f48504"},{url:"pwa-192x192.png",revision:"65f6c00ff3d88d8371df0480c1ba0272"},{url:"pwa-512x512.png",revision:"20a2db7d5040eb315e6acf49c6983de9"},{url:"manifest.webmanifest",revision:"37e8d18026b05432f623fc5efac2b4b1"}],{}),e.cleanupOutdatedCaches(),e.registerRoute(new e.NavigationRoute(e.createHandlerBoundToURL("index.html")))}));