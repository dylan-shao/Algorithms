/*
* DO-NOT-REPEAT-MYSELF series: https://github.com/dylan-shao/DO-NOT-REPEAT-MYSELF
*
* This file will iterate the folders in this repo, and automatically generate a README.md
* with Links and file name in there, when commit the code.
* Click the repo name on top to see what the README.md looks like!
*/

const fs = require('fs');
const header =
  '> This README.md is created automatically when commit the code, used [`pre-commit`](https://www.npmjs.com/package/pre-commit) to hook up [this script](https://github.com/dylan-shao/Algorithms/blob/master/index.js), which create a README.md by iterating the folders using the `nodejs` `fs` module. \n' +
  '## Algorithms\n' +
  'This is a Algorithms Practice Repo to help me understanding data structures.\n' +
  'All algorithms are written in Java, JavaScript and Python.' +
  '\n' +
  '\n' +
  '----------' +
  '\n' +
  '\n' +
  '|Algorithm|  Java  | Python  |  JavaScript\n' +
  '|--- |:--------------:| :-------:|  :---:\n';

fs.writeFileSync('README.md', header);

let javaFiles = 0;
let pyFiles = 0;
let jsFiles = 0;

function getUrl(path, repoName = 'test_watch_files_create_readme', branchName = 'master') {
  return `https://github.com/dylan-shao/${repoName}/blob/${branchName}/${path}`;
}

(function f(dir) {
  const filesOrFolders = fs.readdirSync(dir);
  for (let i = 0; i < filesOrFolders.length; i++) {
    const fileOrFolder = filesOrFolders[i];

    // ignore unwanted files or folders
    if (!/^(node_modules)|^package.*$|^index\.js.*$|^README\.md.*$|((^|[\/\\])\..)/.test(fileOrFolder)) {
      const fileOrFolderName = dir + '/' + fileOrFolder;

      /*---------------------if is directory-------------------*/
      if (fs.statSync(fileOrFolderName).isDirectory()) {
        // fileOrFolderName start with ./path/to...., so remove it
        const folderName = fileOrFolderName.replace('./', '');

        // only if it's the 1st layer folder, then we create a row with folder name and * in there
        if (folderName.indexOf('/') < 0 && folderName.indexOf('.') < 0) {
          const content = `|**${folderName}**|*********|*********|*********\n`;
          fs.appendFile('README.md', content, function(err) {
            if (err) throw err;
          });
        }

        //Recursion
        f(fileOrFolderName);
        /*-------------------------------------------------------*/
      } else {
        /*---------------------if is file----------------------*/
        const defaultName = 'Todo...';
        let javaName = defaultName;
        let javaPath;
        let pyName = defaultName;
        let pyPath;
        let jsName = defaultName;
        let jsPath;
        // if this is file, get parent folder, check all files at once and save them into one line content
        const files = fs.readdirSync(dir);
        files.forEach(file => {
          const fileName = (encodeURIComponent(dir) + '/' + file).replace('./', '');
          if (file.indexOf('.java') >= 0) {
            javaFiles++;
            javaName = file;
            javaPath = getUrl(fileName);
          } else if (file.indexOf('.py') >= 0) {
            pyFiles++;
            pyName = file;
            pyPath = getUrl(fileName);
          } else if (file.indexOf('.js') >= 0) {
            jsFiles++;
            jsName = file;
            jsPath = getUrl(fileName);
          }
        });
        const content = `|| [${javaName}](${javaPath})|[${pyName}](${pyPath})|[${jsName}](${jsPath})\n`;
        fs.appendFile('README.md', content, function(err) {
          if (err) throw err;
        });

        // if is file, break out of the loop, because we already jumped out to the parent and appended the content above
        break;
        /*----------------------------------------------------*/
      }
    }
  }
})('.');
const summary = `\n\nTotally ${javaFiles} java files, ${pyFiles} python files, ${jsFiles} JaaScript files`;
fs.appendFile('README.md', summary, function(err) {
  if (err) throw err;
});
console.log(summary);
