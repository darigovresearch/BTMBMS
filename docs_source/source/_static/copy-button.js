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
        
        let resetTimeout;
        
        copyButton.addEventListener('click', function() {
            clearTimeout(resetTimeout);
            
            const codeElement = codeBlock.querySelector('pre');
            const codeText = codeElement ? codeElement.textContent : '';
            
            navigator.clipboard.writeText(codeText).then(function() {
                copyButton.textContent = 'Copied';
                copyButton.classList.add('copied');
                copyButton.classList.remove('copy-failed');
                
                resetTimeout = setTimeout(function() {
                    copyButton.textContent = 'Copy';
                    copyButton.classList.remove('copied');
                }, 1500);
            }).catch(function(err) {
                console.error('Failed to copy text: ', err);
                copyButton.textContent = 'Failed';
                copyButton.classList.remove('copied');
                copyButton.classList.add('copy-failed');
                
                resetTimeout = setTimeout(function() {
                    copyButton.textContent = 'Copy';
                    copyButton.classList.remove('copy-failed');
                }, 1500);
            });
        });
    });
});
