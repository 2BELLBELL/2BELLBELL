import { calculateInvestmentResults, formatter } from "../util/investment.js"

export default function Results({ input }) {
    const resulteData = calculateInvestmentResults(input)
    const initialInvestment = 
        resulteData[0].valueEndOfYear - 
        resulteData[0].interest -
        resulteData[0].annualInvestment

    return (
        <table id="result">
            <thead>
                <tr>
                    <th>Year</th>
                    <th>Investment Value</th>
                    <th>Interest (Year)</th>
                    <th>Total Interest</th>
                    <th>Invested Capital</th>
                </tr>
            </thead>
            <tbody>
                {resulteData.map((yearData) => {
                    const totalInterst = 
                        yearData.valueEndOfYear - 
                        yearData.annualInvestment * yearData.year -
                        initialInvestment;
                    const totalAmountInvested = yearData.valueEndOfYear - totalInterst
                    return <tr key={yearData.year}>
                        <td>{yearData.year}</td>
                        <td>{formatter.format(yearData.valueEndOfYear)}</td>
                        <td>{formatter.format(yearData.interest)}</td>
                        <td>{formatter.format(totalInterst)}</td>
                        <td>{formatter.format(totalAmountInvested)}</td>
                    </tr>
                })}
            </tbody>
        </table>
    )
}