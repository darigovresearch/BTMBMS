document.addEventListener('DOMContentLoaded', function() {
    const codeBlocks = document.querySelectorAll('div.highlight');
    
    codeBlocks.forEach(function(codeBlock) {
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.textContent = 'Copy';
        copyButton.setAttribute('aria-label', 'Copy code to clipboard');
        
        const wrapper = document.createElement('div');
        wrapper.className = 'code-block-wrapper';
        
        codeBlock.parentNode.insertBefore(wrapper, codeBlock);
        wrapper.appendChild(codeBlock);
        wrapper.appendChild(copyButton);
        
        copyButton.addEventListener('click', function() {
            const codeElement = codeBlock.querySelector('pre');
            const codeText = codeElement.textContent;
            
            navigator.clipboard.writeText(codeText).then(function() {
                copyButton.textContent = 'Copied';
                copyButton.classList.add('copied');
                
                setTimeout(function() {
                    copyButton.textContent = 'Copy';
                    copyButton.classList.remove('copied');
                }, 1500);
            }).catch(function(err) {
                console.error('Failed to copy text: ', err);
                copyButton.textContent = 'Failed';
                setTimeout(function() {
                    copyButton.textContent = 'Copy';
                }, 1500);
            });
        });
    });
});
