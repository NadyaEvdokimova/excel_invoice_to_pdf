from setuptools import setup

setup(
    name='excel_invoice_to_pdf',
    packages=['invoicing'],
    version='1.0.0',
    license='MIT',
    description='This package can be used to convert Excel invoices to PDF invoices.',
    author='Nadja Evdokimova',
    author_email='test@example.com',
    url='https://github.com/NadyaEvdokimova/excel_invoice_to_pdf',
    keywords=['invoice', 'excel', 'pdf'],
    install_requires=['pandas', 'fpdf', 'openpyxl'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
