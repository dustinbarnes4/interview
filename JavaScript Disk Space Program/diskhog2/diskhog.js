const fs = require('fs')
const chalk = require('chalk')

console.log("Running diskHog")

let args = null

// Global variables for threshold command prompt input. Threshold size is set at 1000000 to filter anything less than a million bytes * the number specified by the threshold input
let threshold = 0
const THRESHOLD_SIZE = 1000000

function parseArgs() {
    args = process.argv.slice(2);
}

function dirSizeSum(dirEntry) {
    let childrenSizeSum = 0
    if (dirEntry.children) {
        dirEntry.children.forEach(child => {
            if (child.children) dirSizeSum(child)
            childrenSizeSum += child.size
        })
    return childrenSizeSum
    }
}

function gatherDirInfo(path) {
    const MINIMUM_BLOCKS = 1
    const BLOCK_SIZE = 4096
    let dirEntriesArray = []
    let dirEntriesObjects = fs.readdirSync(path, {withFileTypes: true})
    for (let entryObject of dirEntriesObjects) {
        let dirEntry = {
            name: entryObject.name,
            size: (fs.statSync(`${path}\\${entryObject.name}`).size < BLOCK_SIZE ? MINIMUM_BLOCKS : Math.ceil(fs.statSync(`${path}\\${entryObject.name}`).size / BLOCK_SIZE)) * BLOCK_SIZE
        }
        if (entryObject.isDirectory()) {
            dirEntry.children = gatherDirInfo(`${path}\\${dirEntry.name}`)
            dirEntry.size = dirSizeSum(dirEntry)
        }
        dirEntriesArray.push(dirEntry)
    }
    return dirEntriesArray
}

function printDirEntries(dirEntry) {
    console.group()
    if (dirEntry.children) {
        if (dirEntry.size > threshold * THRESHOLD_SIZE) console.log(`(${dirEntry.size.toLocaleString('en-US', {maximumFractionDigits : 2})} B) ` + chalk.magentaBright(`${dirEntry.name}`))
        dirEntry.children.forEach(printDirEntries)
    } else {
        if (dirEntry.size > threshold * THRESHOLD_SIZE) console.log(`(${dirEntry.size.toLocaleString('en-US', {maximumFractionDigits : 2})} B) ` + chalk.cyanBright(`${dirEntry.name}`))
    }
    console.groupEnd()
}

function printDirEntriesMetric(dirEntry) {
    const KILO = 1000
    const MEGA = 1000000
    const GIGA = 1000000000
    // Below uses a multiple ternary operator to determine how best to print the size of the file in metrics. Then adds the appropriate suffix at the end.
    // If the file is within the kilobytes range, it will not display any decimal.
    let sizeMetric = (dirEntry.size / GIGA) > 1 ? `(${(dirEntry.size / GIGA).toLocaleString('en-US', {maximumFractionDigits : 2})} GB`
        : (dirEntry.size / MEGA) > 1 ? `${(dirEntry.size / MEGA).toLocaleString('en-US', {maximumFractionDigits : 2})} MB`
        : `${Math.floor(dirEntry.size / KILO)} KB`

    console.group()
    if (dirEntry.children) {
        if (dirEntry.size > threshold * THRESHOLD_SIZE) console.log(`(${sizeMetric}) ` + chalk.magentaBright(`${dirEntry.name}`))
        dirEntry.children.forEach(printDirEntriesMetric)
    } else {
        if (dirEntry.size > threshold * THRESHOLD_SIZE)console.log(`(${sizeMetric}) ` + chalk.cyanBright(`${dirEntry.name}`))
    }
    console.groupEnd()
}

function sortDirEntries(dirEntries, alpha) {
    dirEntries.forEach(entry => {if (entry.children) sortDirEntries(entry.children, alpha)})
    alpha ? dirEntries.sort((a, b) => (a.name > b.name) ? 1 : -1) : dirEntries.sort((a, b) => (a.size < b.size) ? 1 : -1)
}

function main() {
    // Gain input. Parse command line prompt
    parseArgs()

    let helpFile = fs.readFileSync('.\\help.txt', 'utf-8')

    // Below uses guard clause style to return out of main in the event of a user help request. Will not process further in this case. 
    if (args.includes('-h')) return console.log(helpFile)
    else if (args.includes('--help')) return console.log(helpFile)
    
    let path = __dirname // Default path to current directory if no path is passed in
    if (args.includes('-p')) path = args[args.findIndex(arg => arg === '-p') + 1]
    if (args.includes('--path')) path = args[args.findIndex(arg => arg === '--path') + 1]
    
    let metricBool = false
    if (args.includes('-m')) metricBool = true
    if (args.includes('--metric')) metricBool = true

    if (args.includes('-t')) {
        if (isNaN(args[args.findIndex(arg => arg === '-t') + 1])) threshold = 1
        else threshold = args[args.findIndex(arg => arg === '-t') + 1]
    }
    if (args.includes('--threshold')) {
        if (isNaN(args[args.findIndex(arg => arg === '--threshold') + 1])) threshold = 1
        else threshold = args[args.findIndex(arg => arg === '--threshold') + 1]
    }

    // Traverse directory subtree and build data structure
    let dirEntries = gatherDirInfo(path)

    // args.findIndex returns -1 if 'alpha' is not found. sortDirEntries takes an array of entries and a bool for whether to sort alphabetically as an argument. If alpha is found, then true will be passed to the sort function.
    if (args.includes('-s')) args.findIndex(arg => arg === 'alpha') === -1 ? sortDirEntries(dirEntries, false) : sortDirEntries(dirEntries, true)
    if (args.includes('--sort')) args.findIndex(arg => arg === 'alpha') === -1 ? sortDirEntries(dirEntries, false) : sortDirEntries(dirEntries, true)

    //3. Output file names and sizes from structure
    
    // metricBook will be true if -m or --metric were command line prompts which will call the metrics version of print, otherwise will default to printing bytes
    metricBool ? dirEntries.forEach(printDirEntriesMetric) : dirEntries.forEach(printDirEntries) 
    
}

main()