/*
* DO-NOT-REPEAT-MYSELF series: https://github.com/dylan-shao/DO-NOT-REPEAT-MYSELF
*
* This file will iterate the folders in this repo, and automatically generate a README.md
* with Links and file name in there, when commit the code.
* Click the repo name on top to see what the README.md looks like!
*/

/* TODO: support multiple items in one table cell,
 *       if I have two or more .java in one folder, this script will only show one .java file
 *       to show multiple rows in one cell, use <br>, and refactor use array to handle multiple
**/

const fs = require('fs');
const header =
  '> This README.md is created automatically when commit the code, used [`pre-commit`](https://www.npmjs.com/package/pre-commit) to hook up [this script to create a README.md by iterating the folders using the `nodejs` `fs` module](https://github.com/dylan-shao/Algorithms/blob/master/index.js). \n' +
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
const emojiForFolder = ':seedling::seedling::seedling:';
const emojiForSeperation = ':wavy_dash::wavy_dash::wavy_dash::wavy_dash:';
const defaultName = 'Todo...';

(function f(dir) {
  const filesOrFolders = fs.readdirSync(dir);
  for (let i = 0; i < filesOrFolders.length; i++) {
    const fileOrFolder = filesOrFolders[i];

    // ignore unwanted files or folders
    if (
      !/^(node_modules)|^package.*$|^index\.js.*$|^README\.md.*$|((^|[\/\\])\..)/.test(fileOrFolder)
    ) {
      const fileOrFolderName = dir + '/' + fileOrFolder;

      /*---------------------if is directory-------------------*/
      if (fs.statSync(fileOrFolderName).isDirectory()) {
        // fileOrFolderName start with ./path/to...., so remove it
        const folderName = fileOrFolderName.replace('./', '');

        // only if it's the 1st layer folder, then we create a row with folder name and * in there
        if (folderName.indexOf('/') < 0 && folderName.indexOf('.') < 0) {
          const content = `|${emojiForFolder}**${folderName}**${emojiForFolder}|${emojiForSeperation}|${emojiForSeperation}|${emojiForSeperation}\n`;
          _append(content);
        }

        //Recursion
        f(fileOrFolderName);
        /*-------------------------------------------------------*/
      } else {
        /*---------------------if is file----------------------*/
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
            javaPath = _getUrl(fileName);
          } else if (file.indexOf('.py') >= 0) {
            pyFiles++;
            pyName = file;
            pyPath = _getUrl(fileName);
          } else if (file.indexOf('.js') >= 0) {
            jsFiles++;
            jsName = file;
            jsPath = _getUrl(fileName);
          }
        });
        const questionName = '`*' + `${dir.substr(dir.lastIndexOf('/') + 1)}` + '*`';
        const content =
          `|${questionName}` +
          `|${_getCellContent(javaName, javaPath)}` +
          `|${_getCellContent(pyName, pyPath)}` +
          `|${_getCellContent(jsName, jsPath)}\n`;

        _append(content);

        // if is file, break out of the loop, because we already jumped out to the parent and appended the content above
        break;
        /*----------------------------------------------------*/
      }
    }
  }
})('.');

function _getUrl(path, repoName = 'Algorithms', branchName = 'master') {
  return `https://github.com/dylan-shao/${repoName}/blob/${branchName}/${path}`;
}

function _append(content) {
  fs.appendFile('README.md', content, function(err) {
    if (err) throw err;
  });
}

function _getCellContent(name, path) {
  if (name === defaultName) {
    return defaultName;
  }
  return `[${name}](${path})`;
}

const summary = `\n\nTotally ${javaFiles} Java files, ${pyFiles} Python files, ${jsFiles} JavaScript files`;
_append(summary);

console.log(summary);
